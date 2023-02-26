package me.dio.stack.kt

class mutable_stack<E>(vararg items: E) {	// creates a class that can receive any type of element
    private val elements = items.toMutableList()
    fun push(element: E) = elements.add(element)	// adds an element to the list
    fun peek(): E = elements.last()		// shows the last element
    fun pop(): E = elements.removeAt(elements.size - 1)		// removes the last element
    fun is_empty() = elements.isEmpty()		// verifies if the list is empty
    fun size() = elements.size
    override fun toString() = "mutable_stack(${elements.joinToString()})"	// returns this in the print
}

fun main(){
    fun <E> mutable_stack_of(vararg elements: E) = mutable_stack(*elements)	// generic function
    val stack = mutable_stack("A", "B", "C")
    val stack2 = mutable_stack_of<String>("A", "B", "C")
    println("Inicial stack: $stack")
    println("pushing a value ...")
    stack.push("D")
    println(stack)
    
    println("peek(): ${stack.peek()}") // shows the last value without removing it
    println(stack)
    
    for (i in 1..stack.size()){
        println("pop(): ${stack.pop()}")
        println(stack)
    }
}
