package me.dio.lists.kt 

val system_users: MutableList<Int> = mutableListOf(1,2,3)	// storages a mutable list inside a val
val sudoers: List<Int> = system_users	// creates a view of system_users that is imutable

fun add_system_user(new_user: Int){
    system_users.add(new_user)	// adds to the list
}

fun get_sudoers(): List<Int>{
    return sudoers
}

fun main(){
    println(sudoers)
    add_system_user(4)	// the original list receives a new user and the other list is updated
    println(sudoers) 
    get_sudoers().forEach {	// get_sudoers returns a list so you can use forEach
        i -> println("USER: $i")
    }
    // get_sudoers.add(5) this generates an error because sudoers is read only (a view of the original list)
}
