#include <stdbool.h>
#include <stdlib.h>

#define STACK_SIZE 10000

// Structure for the stack
typedef struct {
    char* items;
    int top;
} Stack;

// Initialize the stack
Stack* createStack() {
    Stack* stack = (Stack*)malloc(sizeof(Stack));
    stack->items = (char*)malloc(STACK_SIZE * sizeof(char));
    stack->top = -1;
    return stack;
}

// Push an item onto the stack
void push(Stack* stack, char item) {
    stack->items[++(stack->top)] = item;
}

// Pop an item from the stack
char pop(Stack* stack) {
    return stack->items[(stack->top)--];
}

// Check if the stack is empty
bool isEmpty(Stack* stack) {
    return stack->top == -1;
}

// Peek at the top item of the stack
char peek(Stack* stack) {
    return stack->items[stack->top];
}

// Free the stack
void freeStack(Stack* stack) {
    free(stack->items);
    free(stack);
}

// Function to check if the string is valid
bool isValid(char* s) {
    Stack* stack = createStack();
    
    while (*s) {
        char c = *s++;
        
        if (c == '(' || c == '{' || c == '[') {
            push(stack, c);
        } else if (c == ')' || c == '}' || c == ']') {
            if (isEmpty(stack)) {
                freeStack(stack);
                return false;
            }
            char top = pop(stack);
            if ((c == ')' && top != '(') ||
                (c == '}' && top != '{') ||
                (c == ']' && top != '[')) {
                freeStack(stack);
                return false;
            }
        }
    }
    
    bool result = isEmpty(stack);
    freeStack(stack);
    return result;
}