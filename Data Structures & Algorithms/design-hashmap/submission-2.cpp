class MyHashMap {
    vector<list<pair<int,int>>> _hm;
    int siz=1e6+1;
public:
    MyHashMap(){
    _hm.resize(siz);
    }

    int hash(int key){
        return key%siz;
    }

    list<pair<int,int>> :: iterator search(int key){
        int i=hash(key);
       list<pair<int,int>> :: iterator it=_hm[i].begin(); 
       while(it!=_hm[i].end()){
        if(it->first==key) return it;
        else it++;
       }
       return it;
    }

    void put(int key, int value) {
        int i=hash(key);
        list<pair<int,int>> :: iterator it=search(key);
        if(it!=_hm[i].end()){
        it->second=value;
        return;
        }
        
        _hm[i].push_back({key,value});    
    }
    
    int get(int key) {
        int i=hash(key);
        list<pair<int,int>> :: iterator it=search(key);
        if(it==_hm[i].end()) return -1;
        else return it->second;
    }
    
    void remove(int key) {
       int i=hash(key);
       list<pair<int,int>> :: iterator it=search(key);     
       if(it!=_hm[i].end()){
        _hm[i].erase(it);
       }        
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */