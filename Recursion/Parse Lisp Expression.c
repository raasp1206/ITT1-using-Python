#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_VARS 100
#define MAX_VAR_LEN 25

typedef struct {
    char keys[MAX_VARS][MAX_VAR_LEN];
    int values[MAX_VARS];
    int size;
} Env;

const char* ptr;

int evaluateInternal(Env* parent_env);

void parseToken(char* token) {
    while (*ptr == ' ') ptr++;
    
    int len = 0;
    if (*ptr == '(' || *ptr == ')') {
        token[len++] = *ptr++;
    } else {
        while (*ptr && *ptr != ' ' && *ptr != ')' && *ptr != '(') {
            token[len++] = *ptr++;
        }
    }
    token[len] = '\0';
}

int lookup(Env* env, const char* var) {
    for (int i = env->size - 1; i >= 0; i--) {
        if (strcmp(env->keys[i], var) == 0) {
            return env->values[i];
        }
    }
    return 0;
}

int parseNext(Env* env) {
    while (*ptr == ' ') ptr++;
    
    if (*ptr == '(') {
        return evaluateInternal(env);
    }
    
    char token[MAX_VAR_LEN];
    parseToken(token);
    
    if (islower(token[0])) {
        return lookup(env, token);
    }
    
    return atoi(token);
}

int evaluateInternal(Env* parent_env) {
    while (*ptr == ' ') ptr++;
    if (*ptr == '(') ptr++;
    
    char command[MAX_VAR_LEN];
    parseToken(command);
    
    int result = 0;
    
    if (strcmp(command, "add") == 0) {
        int e1 = parseNext(parent_env);
        int e2 = parseNext(parent_env);
        result = e1 + e2;
    } 
    else if (strcmp(command, "mult") == 0) {
        int e1 = parseNext(parent_env);
        int e2 = parseNext(parent_env);
        result = e1 * e2;
    } 
    else if (strcmp(command, "let") == 0) {
        Env child_env;
        child_env.size = parent_env->size;
        for (int i = 0; i < parent_env->size; i++) {
            strcpy(child_env.keys[i], parent_env->keys[i]);
            child_env.values[i] = parent_env->values[i];
        }
        
        while (1) {
            while (*ptr == ' ') ptr++;
            
            if (*ptr == '(') {
                result = evaluateInternal(&child_env);
                break;
            }
            
            char var_or_val[MAX_VAR_LEN];
            parseToken(var_or_val);
            
            while (*ptr == ' ') ptr++;
            
            if (*ptr == ')') {
                if (islower(var_or_val[0])) {
                    result = lookup(&child_env, var_or_val);
                } else {
                    result = atoi(var_or_val);
                }
                break;
            }
            
            int val = parseNext(&child_env);
            
            int found = 0;
            for (int i = child_env.size - 1; i >= 0; i--) {
                if (strcmp(child_env.keys[i], var_or_val) == 0) {
                    child_env.values[i] = val;
                    found = 1;
                    break;
                }
            }
            if (!found) {
                strcpy(child_env.keys[child_env.size], var_or_val);
                child_env.values[child_env.size] = val;
                child_env.size++;
            }
        }
    }
    
    while (*ptr == ' ') ptr++;
    if (*ptr == ')') ptr++;
    
    return result;
}

int evaluate(char* expression) {
    ptr = expression;
    Env initial_env;
    initial_env.size = 0;
    return evaluateInternal(&initial_env);
}
