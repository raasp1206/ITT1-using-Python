#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TERMS 2000
#define MAX_VARS 15
#define MAX_VAR_LEN 25

typedef struct {
    int coef;
    char vars[MAX_VARS][MAX_VAR_LEN];
    int var_count;
} Term;

typedef struct {
    Term terms[MAX_TERMS];
    int term_count;
} Poly;

int compareStrings(const void* a, const void* b) {
    return strcmp((const char*)a, (const char*)b);
}

int compareTerms(const void* a, const void* b) {
    const Term* ta = (const Term*)a;
    const Term* tb = (const Term*)b;
    
    if (ta->var_count != tb->var_count) {
        return tb->var_count - ta->var_count;
    }
    
    for (int i = 0; i < ta->var_count; i++) {
        int cmp = strcmp(ta->vars[i], tb->vars[i]);
        if (cmp != 0) return cmp;
    }
    return 0;
}

int sameVariables(const Term* t1, const Term* t2) {
    if (t1->var_count != t2->var_count) return 0;
    for (int i = 0; i < t1->var_count; i++) {
        if (strcmp(t1->vars[i], t2->vars[i]) != 0) return 0;
    }
    return 1;
}

Poly simplifyPoly(Poly p) {
    Poly res;
    res.term_count = 0;
    
    for (int i = 0; i < p.term_count; i++) {
        if (p.terms[i].var_count > 1) {
            qsort(p.terms[i].vars, p.terms[i].var_count, MAX_VAR_LEN, compareStrings);
        }
    }
    
    qsort(p.terms, p.term_count, sizeof(Term), compareTerms);
    
    for (int i = 0; i < p.term_count; i++) {
        if (p.terms[i].coef == 0) continue;
        
        if (res.term_count > 0 && sameVariables(&res.terms[res.term_count - 1], &p.terms[i])) {
            res.terms[res.term_count - 1].coef += p.terms[i].coef;
            if (res.terms[res.term_count - 1].coef == 0) {
                res.term_count--;
            }
        } else {
            res.terms[res.term_count++] = p.terms[i];
        }
    }
    return res;
}

Poly addPoly(Poly p1, Poly p2) {
    Poly res;
    res.term_count = 0;
    for (int i = 0; i < p1.term_count; i++) res.terms[res.term_count++] = p1.terms[i];
    for (int i = 0; i < p2.term_count; i++) res.terms[res.term_count++] = p2.terms[i];
    return simplifyPoly(res);
}

Poly subPoly(Poly p1, Poly p2) {
    Poly res;
    res.term_count = 0;
    for (int i = 0; i < p1.term_count; i++) res.terms[res.term_count++] = p1.terms[i];
    for (int i = 0; i < p2.term_count; i++) {
        Term t = p2.terms[i];
        t.coef = -t.coef;
        res.terms[res.term_count++] = t;
    }
    return simplifyPoly(res);
}

Poly mulPoly(Poly p1, Poly p2) {
    Poly res;
    res.term_count = 0;
    for (int i = 0; i < p1.term_count; i++) {
        for (int j = 0; j < p2.term_count; j++) {
            Term t;
            t.coef = p1.terms[i].coef * p2.terms[j].coef;
            t.var_count = 0;
            
            for (int k = 0; k < p1.terms[i].var_count; k++) {
                strcpy(t.vars[t.var_count++], p1.terms[i].vars[k]);
            }
            for (int k = 0; k < p2.terms[j].var_count; k++) {
                strcpy(t.vars[t.var_count++], p2.terms[j].vars[k]);
            }
            res.terms[res.term_count++] = t;
        }
    }
    return simplifyPoly(res);
}

// Global Variables used by the parsing functions
const char* expr_ptr;
char** eval_vars;
int* eval_ints;
int eval_size;

Poly parseExpression();

Poly parseFactor() {
    Poly res;
    res.term_count = 0;
    
    while (*expr_ptr == ' ') expr_ptr++;
    
    if (*expr_ptr == '(') {
        expr_ptr++;
        res = parseExpression();
        while (*expr_ptr == ' ') expr_ptr++;
        if (*expr_ptr == ')') expr_ptr++;
        return res;
    }
    
    Term t;
    t.var_count = 0;
    
    if (isdigit(*expr_ptr)) {
        int val = 0;
        while (isdigit(*expr_ptr)) {
            val = val * 10 + (*expr_ptr - '0');
            expr_ptr++;
        }
        t.coef = val;
    } else {
        char name[MAX_VAR_LEN];
        int len = 0;
        while (islower(*expr_ptr)) {
            name[len++] = *expr_ptr++;
        }
        name[len] = '\0';
        
        int mapped = 0;
        for (int i = 0; i < eval_size; i++) {
            if (strcmp(eval_vars[i], name) == 0) {
                t.coef = eval_ints[i];
                mapped = 1;
                break;
            }
        }
        if (!mapped) {
            t.coef = 1;
            strcpy(t.vars[0], name);
            t.var_count = 1;
        }
    }
    
    res.terms[res.term_count++] = t;
    return res;
}

Poly parseTerm() {
    Poly res = parseFactor();
    while (1) {
        while (*expr_ptr == ' ') expr_ptr++;
        if (*expr_ptr == '*') {
            expr_ptr++;
            Poly next_factor = parseFactor();
            res = mulPoly(res, next_factor);
        } else {
            break;
        }
    }
    return res;
}

Poly parseExpression() {
    Poly res = parseTerm();
    while (1) {
        while (*expr_ptr == ' ') expr_ptr++;
        if (*expr_ptr == '+' || *expr_ptr == '-') {
            char op = *expr_ptr++;
            Poly next_term = parseTerm();
            if (op == '+') {
                res = addPoly(res, next_term);
            } else {
                res = subPoly(res, next_term);
            }
        } else {
            break;
        }
    }
    return res;
}

char** basicCalculatorIV(char* expression, char** evalvars, int evalvarsSize, int* evalints, int evalintsSize, int* returnSize) {
    expr_ptr = expression;
    eval_vars = evalvars;
    eval_ints = evalints;
    eval_size = evalvarsSize;
    
    Poly final_poly = parseExpression();
    
    char** result = (char**)malloc(sizeof(char*) * final_poly.term_count);
    int valid_count = 0;
    
    for (int i = 0; i < final_poly.term_count; i++) {
        Term t = final_poly.terms[i];
        
        // Skip terms with a coefficient of 0
        if (t.coef == 0) {
            continue;
        }
        
        result[valid_count] = (char*)malloc(sizeof(char) * 500); 
        
        if (t.var_count == 0) {
            sprintf(result[valid_count], "%d", t.coef);
        } else {
            char buffer[500]; 
            sprintf(buffer, "%d", t.coef);
            for (int j = 0; j < t.var_count; j++) {
                strcat(buffer, "*");
                strcat(buffer, t.vars[j]);
            }
            strcpy(result[valid_count], buffer);
        }
        valid_count++;
    }
    
    *returnSize = valid_count;
    return result;
}
