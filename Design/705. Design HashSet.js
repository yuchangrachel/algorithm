class MyHashSet {
    constructor(){
        this.arr = []
    }
    add(key){
        if (!this.arr.includes(key)){
            this.arr.push(key)
        }
    }
    remove(key){
        if (this.arr.includes(key)){
            this.arr = this.arr.filter((value, index, arr) =>value != key);      
        }
    }
    contains(key){
        if (this.arr.includes(key)){
            return true
        }
        else 
            return false
    }
    
}