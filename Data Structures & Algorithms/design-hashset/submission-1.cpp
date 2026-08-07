class MyHashSet {
    vector<int> hs; 
public:
    
    MyHashSet() {
      
    }
    
    void add(int key) {
        if(!contains(key)) hs.push_back(key);
    }
    
    void remove(int key) {
            hs.erase(::std::remove(hs.begin(),hs.end(),key),hs.end());
    }
    
    bool contains(int key) {

        if(find(hs.begin(),hs.end(),key)!=hs.end()){
            return true;
        }
        else return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */