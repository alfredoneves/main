package me.dio.data_classes.kt

data class User(val name: String, val id: Int) {	// creates a data class to storage values
    override fun equals(other: Any?): Boolean {	// this is a native function that now is altered
        return other is User && other.id == this.id	// compares the class and the id
    }
}

fun main() {
    val user: User = User("Admin", 0)
    val second_user: User = User("Admin", 0)
    val third_user: User = User("Max", 1)
    println(user)
    println(user == second_user)	// uses the override comparisson
    println(user == third_user)
    
    // testing comparisson
    val user_test1: User = User ("Admin", 88)
    println("comparisson test1: ${user == user_test1}")
    val user_test2: User = User ("test", 0)
    println("comparisson test2: ${user == user_test2}")
    
    // hashCode function
    println(user.hashCode())	// generates a hash
    println(second_user.hashCode())
    println(third_user.hashCode())
    
    //copy function
    println(user.copy())	// makes a structural copy
    println(user === user.copy())
    println(user.copy("Max"))	// the copy can be altered
    println(user.copy(id = 4))
    println("name = ${user.component1()}")	// a second way to access the attribute (like user.name)
}
