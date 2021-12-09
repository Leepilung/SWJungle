#include <stdio.h>
#include <stdlib.h>
// 포인터를 사용해야 데이터 낭비가 없음.
/* 이진 탐색트리란?
1. 모든 원소는 유일한 키 값을 가진다.
2. 왼쪽 서브트리의 모든 원소들은 루트의 키보다 작은 값을 갖는다.
3. 오른쪽 서브트리의 모든 원소들은 루트의 키보다 큰 값을 갖는다.
4. 왼쪽 서브트리와 오른쪽 서브트리도 이진탐색트리이다.

링크 : https://www.youtube.com/watch?v=ESqeK-ACHkU&ab_channel=%EC%B4%88%EC%9D%B4%EC%8A%A4%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D
*/


typedef char data;
typedef struct _Node {
    char key;
    struct _Node* left;
    struct _Node* right;
} Node;

Node* searchBST(Node* root, char x) {
    Node* p = root;
    while (p != NULL); {
        if (p->key == x)
        return p;
        else if (p -> key < x)
        p = p->right;
        else
        p = p->left;
    }
    return NULL;
}

Node* insertBST(Node* root, char x) {
    Node* p = root;
    Node* parent = NULL;
    while (p != NULL) {
        parent = p;
        if (p->key == x)  {
        printf('같은 키값이 있습니다.\n');
        return p;
        }
        else if (p -> key < x)
        p = p->right;
        else
        p = p->left;
    }
    // 새 노드 할당
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode-> key = x;
    newNode ->left = newNode-> right = NULL;

    // parent의 자식으로 새 노드 붙이기.
    if (parent != NULL) {
        if (parent->key < newNode->key)
            parent->right = newNode;
        else
            parent->left = newNode;
    }
    return newNode;
}

Node* deleteBST(Node* root, char x) {
    Node* p = root;
    Node* parent = NULL;
    while ((p != NULL) && (p->key != x)) {
        parent = p;
        if (p->key < x)
        p = p->right;
        else
        p = p->left;
    }
    if (p == NULL) {
        printf("찾는 노드가 없습니다.\n");
        return root;
    }

    if (p -> left == NULL && p->right == NULL) { // 차수가 0인 부분
        if (parent == NULL)
        root = NULL;
        else {
        if (parent -> left == p)
            parent -> left = NULL;
        else
            parent -> right = NULL;
        }
    }
    else if (p->left == NULL || p->right == NULL) { // 차수가 1인 경우가 해당
        Node *child = (p->left != NULL) ? p->left : p->right;
        if (parent == NULL)
        root = child;
        else {
        if (parent->left == p)
            parent->left = child;
        else
            parent->right = child;
        }
    }
    else {    // 차수가 2인 경우
        Node* succ_parent = p;
        Node* succ = p->right;
        while (succ -> left != NULL) {
        succ_parent = succ;
        succ = succ->left;
        }
        p->key = succ->key;
        if (succ_parent->left == succ)
        succ_parent->left = succ->right;
        else
        succ_parent->right = succ->right;
        p = succ;
    }

    free(p);
    return root;
    }

    void Inorder(Node* root) {
    if (root == NULL)
        return;
    Inorder(root->left);
    printf("%c",root->key);
    Inorder(root->right);
    }

    int main() {
    Node *root = insertBST(NULL, 'D');
    insertBST(root, 'I');
    insertBST(root, 'A');
    insertBST(root, 'F');
    insertBST(root, 'C');
    insertBST(root, 'G');

    Inorder(root); printf("\n");

    root = deleteBST(root,'G');
    Inorder(root); printf("\n");
    return 0;

}