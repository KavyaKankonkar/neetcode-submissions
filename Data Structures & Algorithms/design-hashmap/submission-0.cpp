class MyHashMap {
    vector<int> _hm;
public:
    MyHashMap():_hm(1000001,-1) {

    }
    
    void put(int key, int value) {
        _hm[key]=value;
    }
    
    int get(int key) {
        return _hm[key];
    }
    
    void remove(int key) {
       _hm[key]=-1;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */