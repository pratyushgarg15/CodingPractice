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

	void insert_at_begin(int val){
		
		SinglyLinkedListNode* newNode = new SinglyLinkedListNode(val);

		if(this->head == nullptr)
			this->head = newNode;

		else{
			newNode->next = this->head;
			this->head = newNode;
		}
			
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

	void delete_at_begin(){
		SinglyLinkedListNode* del = this->head;

		if(this->head == nullptr)
			return ;

		else
			this->head = this->head->next;

		delete del;
	}

	void delete_at_end(){
		SinglyLinkedListNode* follow;
		SinglyLinkedListNode* del = this->head;

		if(this->head == nullptr)
			return ;

		while(del->next != nullptr){
			follow = del;
			del = del->next;
		}
		

		follow->next = nullptr;
		follow = nullptr;

		delete follow;
		delete del;
	}

	void insert_at_pos(int val, int pos){
		SinglyLinkedListNode* newNode = new SinglyLinkedListNode(val);

		if(this->head == nullptr)
			this->head = newNode;

		SinglyLinkedListNode* temp = this->head;

		for(int i=1; i<pos-1 ; i++)
			temp = temp->next;
		
		newNode->next = temp->next;
		temp->next = newNode;

		temp = nullptr;
		delete temp;
	}

	void delete_at_pos(int pos){
		SinglyLinkedListNode* del = this->head;
		SinglyLinkedListNode* follow;

		if(this->head == nullptr)
			return ;

		for(int i=1; i<pos ; i++){
			follow = del;
			del = del->next;		
		}
		follow->next = del->next;
		follow = nullptr;

		delete del;
		delete follow;
	}
		
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
	SinglyLinkedList* list = new SinglyLinkedList();

	list->insert_at_begin(23);
	list->insert_at_begin(78);
	list->insert_at_end(54);
	list->insert_at_end(79);
	list->insert_at_end(90);
	list->insert_at_pos(24,3);

	list->printLinkedList();

	list->delete_at_end();
	list->delete_at_begin();
	list->delete_at_pos(3);

	list->printLinkedList();

}