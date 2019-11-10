#include <iostream>
using namespace std;

class LinkedListNode{
public:
	int data;
	LinkedListNode* next;
	LinkedListNode* prev;

	LinkedListNode(int data){
		this->data = data;
		this->next = nullptr;
		this->prev = nullptr;
	}
};

class LinkedList {
	public :
	LinkedListNode* head;
	LinkedListNode* tail;

	LinkedList(){
		this->head = nullptr;
		this->tail = nullptr;
	}

	void append(int data){
		LinkedListNode* node = new LinkedListNode(data);

		if(this->head == nullptr){
			this->head = node;
			this->tail = node;
		}

		else{
			node->prev = tail;
			node->next = nullptr;
			this->tail->next = node;
			this->tail = node;
		}

	}

	void pop(){
		if(this->head == nullptr){
			return;
		}

		else if(this->head == this->tail){
			LinkedListNode* del = this->head;
			head = nullptr;
			tail = nullptr;
			delete del;
		}

		else{
			LinkedListNode* del = this->tail;
			this->tail = this->tail->prev;
			this->tail->next = nullptr;
			delete del;
		}
	}	

	void printLinkedList(){
		LinkedListNode* temp = this->head;
		while(temp->next != nullptr){
			cout << temp->data << "->"  ;
			temp = temp->next;
		}
		cout << temp->data << endl;
		temp = temp->next;
		free(temp);	
	}
};

int main(){
	LinkedList* stack = new LinkedList();
	stack->append(7);
	stack->append(65);
	stack->append(87);
	stack->append(34);
	stack->append(12);
	stack->append(190);

	stack->printLinkedList();

	stack->pop();
	stack->pop();

	stack->printLinkedList();
}

