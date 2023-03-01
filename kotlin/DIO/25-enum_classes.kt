package me.dio.enum_classes.kt

enum class State(){	// creates a class with limited options
    IDLE, RUNNING, FINISHED
}

enum class Color(val rgb: Int) {
    RED(0xFF0000),
    BLUE(0x0000FF);	// attention to the ;
    
    fun contains_red() = (this.rgb and 0xFF000 != 0)
}

fun main() {
    //state
    val state: State = State.RUNNING
    val message = when (state) {
        State.IDLE -> "IDLE"
        State.RUNNING -> "RUNNING"
        State.FINISHED -> "FINISHED"
        else -> "error"
    }
    println(message)
    
    //color
    val color_red: Color = Color.RED
    println(color_red)
    println("contains red? ${color_red.contains_red()}")
    println(Color.BLUE.contains_red())	// trick without the variable
}
