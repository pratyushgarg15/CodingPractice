#include <iostream>
using namespace std;

class LinkedListNode{
public:	
	int data;
	LinkedListNode* link;

	LinkedListNode(int val){
		this->data = val;
		this->link = nullptr;
	}
};

class XORLinkedList{
public:	
	LinkedListNode* head;

	XORLinkedList(){
		this->head = nullptr;
	}

	LinkedListNode* XOR(LinkedListNode* x , LinkedListNode* y){
		return (LinkedListNode*)((uintptr_t)(x) ^ (uintptr_t)(y));
	}

	void append(int val){
		LinkedListNode* newNode = new LinkedListNode(val);
		
		if(this->head == nullptr){
			this->head = newNode;
			return ;
		}

		if(this->head->link == nullptr){
			this->head->link = newNode;
			newNode->link = this->head;
			return ;
		}

		LinkedListNode* node ;
		LinkedListNode* follow;
		LinkedListNode* temp;
	
		follow = this->head;
		node = follow->link;

		while(node->link != follow){
			temp = follow;
			follow = node;
			node = XOR(temp, node->link);
		}

		node->link = XOR(follow, newNode);
		newNode->link = node;
		
        temp = nullptr;
		node = nullptr;
		follow = nullptr;
		delete node;
		delete follow;
		delete temp;
	}

	void printLinkedList(){

		if(this->head->link == nullptr){
			cout << this->head->data;
			return ;
		}

		LinkedListNode* node ;
		LinkedListNode* follow;
		LinkedListNode* temp;
		
		follow = this->head;
		node = follow->link;

		while(node->link != follow){
			cout << follow->data << "->" ;
			temp = follow;
			follow = node;
			node = XOR(temp, node->link);
		}

		cout << follow->data << "->";
		cout << node->data << endl;

		temp = nullptr;
		node = nullptr;
		follow = nullptr;
		delete node;
		delete follow;
		delete temp;
	}
};

int main(){
	XORLinkedList* list = new XORLinkedList();

	list->append(1);
	list->append(2);
	list->append(3);
	list->append(4);
	list->append(5);

	list->printLinkedList();

}