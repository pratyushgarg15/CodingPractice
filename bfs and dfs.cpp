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

	int remove(){
		if(this->head == nullptr){
			return 0;
		}

		else if(this->head == this->tail){
			LinkedListNode* del = this->head;
			head = nullptr;
			tail = nullptr;
			int data = del->data;
			delete del;
			return data;
		}
		else{
			LinkedListNode* del = this->head;
			this->head = this->head->next;
			this->head->prev = nullptr;
			int data = del->data;
			delete del;
			return data;
		}
	}

	int pop(){
		if(this->head == nullptr){
			return 0;
		}

		else if(this->head == this->tail){
			LinkedListNode* del = this->head;
			head = nullptr;
			tail = nullptr;
			int data = del->data;
			delete del;
			return data;
		}
		else{
			LinkedListNode* del = this->tail;
			this->tail = this->tail->prev;
			this->tail->next = nullptr;
			int data = del->data;
			delete del;
			return data;
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

	void bfs(int s){
		bool visited[this->vertices] = {0};
		LinkedList* queue = new LinkedList();
		queue->insert(s);
		visited[s] = 1;

		while(queue->head != nullptr){
			int vertex = queue->remove();
			LinkedListNode* temp = adjlist[vertex].head;

			while(temp){
				if(!visited[temp->data]){
					queue->insert(temp->data);
					visited[temp->data] = 1;
				}
				temp = temp->next;
			}

			cout << vertex << " ";
		}
		cout << endl;
	}

	void dfs(int s){
		bool visited[this->vertices] = {0};
		LinkedList* stack = new LinkedList();
		stack->insert(s);
		visited[s] = 1;

		while(stack->head != nullptr){
			int vertex = stack->pop();
			LinkedListNode* temp = adjlist[vertex].head;

			while(temp){
				if(!visited[temp->data]){
					stack->insert(temp->data);
					visited[temp->data] = 1;
				}
				temp = temp->next;
			}

			cout << vertex << " ";
		}
        
	}

	~Graph(){
		
		delete adjlist;
	}

};

int main(){

    int v = 5;
	Graph* g1 = new Graph(v) ; 

	g1->addEdge(0,1);
    g1->addEdge(0,2);
    g1->addEdge(1,4);
    g1->addEdge(2,1);
    g1->addEdge(2,3);
    g1->addEdge(3,4);
    g1->addEdge(4,0);
    
	
    g1->printGraph();

    g1->bfs(4);
    g1->dfs(4);

    delete g1;
}