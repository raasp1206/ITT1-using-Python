#include <stdio.h>

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    if (head == NULL || k == 1) {
        return head;
    }

    struct ListNode dummy;
    dummy.next = head;
    struct ListNode* prev_group_end = &dummy;
    struct ListNode* curr = head;

    while (curr != NULL) {
        struct ListNode* check = curr;
        int count = 0;
        while (check != NULL && count < k) {
            check = check->next;
            count++;
        }

        if (count < k) {
            break;
        }

        struct ListNode* prev = NULL;
        struct ListNode* next_node = NULL;
        struct ListNode* group_start = curr;

        for (int i = 0; i < k; i++) {
            next_node = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next_node;
        }

        prev_group_end->next = prev;
        group_start->next = curr;

        prev_group_end = group_start;
    }

    return dummy.next;
}
