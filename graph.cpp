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
		//cout << ":)" << endl;
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

class Graph{
public:
	LinkedList* adjlist;
	int vertices;
	
	Graph(int v){
		vertices = v;
	    adjlist = new LinkedList[v]();
	    //cout << "All Good!!" << endl;
	}

	void addEdge(int src , int dest){
		adjlist[src].insert(dest);
	}

	void printGraph(){
		for(int i = 0 ; i < this->vertices ; i++ ){
			cout << i << "->" ;
			adjlist[i].printLinkedList();
		}
	}

	~Graph(){
		
		delete adjlist;
	}

};

int main(){

    int v = 3;
	Graph* g1 = new Graph(v) ; 

	g1->addEdge(0,1);
	g1->addEdge(0,2);
	g1->addEdge(1,0);
	g1->addEdge(2,1);
	
    g1->printGraph();

    delete g1;
}