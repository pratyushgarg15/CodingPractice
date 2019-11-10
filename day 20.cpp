#include <iostream>
using namespace std;

class SinglyLinkedListNode{
public:	
	int data ;
	SinglyLinkedListNode* next;
	
	SinglyLinkedListNode(int val){	
		this->data = val;
		this->next = nullptr;
	}
};

class SinglyLinkedList{
public:	
	SinglyLinkedListNode* head;

	SinglyLinkedList(){
		this->head = nullptr;
	}

	void insert_at_end(int val){

		SinglyLinkedListNode* newNode = new SinglyLinkedListNode(val);

		if(this->head == nullptr)
			this->head = newNode;

		SinglyLinkedListNode* temp = this->head;

		while(temp->next != nullptr)
			temp = temp->next;

		temp->next = newNode;

	}

	/*void insert_at_end(SinglyLinkedListNode* node){

		SinglyLinkedListNode* newNode = node;

		if(this->head == nullptr)
			this->head = newNode;

		SinglyLinkedListNode* temp = this->head;

		while(temp->next != nullptr)
			temp = temp->next;

		temp->next = newNode;

	}*/

	
		
	void printLinkedList(){
		SinglyLinkedListNode* node = this->head;
		while(node->next != nullptr){
			cout << node->data << "->"  ;
			node = node->next;
		}
		cout << node->data << endl;
		node = node->next;
		delete node;	
	}	
};

int main(){
	SinglyLinkedList* list1 = new SinglyLinkedList();
	SinglyLinkedList* list2 = new SinglyLinkedList();
	
	list1->insert_at_end(3);
	list1->insert_at_end(7);
	list1->insert_at_end(8);
	list1->insert_at_end(9);
	list1->insert_at_end(22);
	list1->insert_at_end(1);

	list2->insert_at_end(12);
	list2->insert_at_end(14);
	list2->insert_at_end(27);
	list2->insert_at_end(1);
	list2->insert_at_end(10);

	//list2->insert_at_end(list1->head->next->next);

	list1->printLinkedList();
	list2->printLinkedList();

}