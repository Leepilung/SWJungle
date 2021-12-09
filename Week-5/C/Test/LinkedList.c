#include <stdio.h>
#include <stdlib.h>

struct NODE { // 연결 리스트의 노드 구조체 정의
  struct NODE * next; // 다음 노드의 주소를 저장할 포인터
  int data; // 데이터를 저장할 멤버 
};

/* 노드의 종류 
- 머리 노드(haed node) : 단일 연결 리스트의 기준점. 헤드라고 부름. 첫 번째 노드를 가리키는 용도, 데이터 저장 안함.
- 노드(node) : 단일 연결 리스트에서 데이터가 저장되는 실제 노드
*/

int main()
{
    struct NODE *head = malloc(sizeof(struct NODE));  // 머리노드 생성
    // 머리노드는 기준점 역할만 함. 데이터 저장 안함
    struct NODE *node1 = malloc(sizeof(struct NODE)); // 첫번째 노드 생성
    head -> next = node1;   // 머리 노드의 next에 첫번째 노드 저장
    node1 -> data = 10;  

    struct NODE *node2 = malloc(sizeof(struct NODE)); // 두번째 노드 생성
    node1 -> next = node2;  // 첫번째 노드의 next에 2번째 노드 저장
    node2 -> data = 20;

    node2 -> next = NULL; // 마지막 노드 다음은 NULL

    struct NODE *curr = head->next; // 순회용 포인터 curr 생성, head->next 저장
    while (curr != NULL)
    {
        printf("%d\n", curr -> data);
        curr = curr -> next;  
    }

    free(node2);
    free(node1);
    free(head);
}