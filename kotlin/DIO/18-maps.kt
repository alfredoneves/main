package me.dio.maps.kt 

const val points: Int = 15	// creates a const that will be used
//below the mutable map is created and it's like a dictionary in python 1:100, 2:200
val accounts: MutableMap<Int, Int> = mutableMapOf(1 to 100, 2 to 100, 3 to 100)
val accounts_report: Map<Int, Int> = accounts	// creates a read only object that mirrors the accounts

fun update_points(account_id: Int){
    if (accounts.containsKey(account_id)) {	// verifies if the id exists in the accounts
        println("updating account $account_id with $points")
        accounts[account_id] = accounts.getValue(account_id) + points	// updates the value of the id
    } else {
        println("account id $account_id doesn't exist")
    }
}

fun report(ac: Map<Int, Int>) {	// receives a map object
    println("report:")
    ac.forEach {	// selects all the elements one by one
        k, v -> println("ID: $k points:$v")
    }
}

fun main(){
    report(accounts_report)
    update_points(1)
    update_points(2)
    update_points(1)
    update_points(4)
    report(accounts_report)
}
