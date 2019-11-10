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

	void insert(int data){
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

	void remove(){
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
			LinkedListNode* del = this->head;
			this->head = this->head->next;
			this->head->prev = nullptr;
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
	LinkedList* queue = new LinkedList();
	queue->insert(7);
	queue->insert(78);
	queue->insert(54);
	queue->insert(32);
	queue->insert(1);
	queue->insert(27);

	queue->printLinkedList();

	queue->remove();
	queue->remove();

	queue->printLinkedList();
}

