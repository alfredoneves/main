package me.dio.sets.kt 

//mutableSetOf != setOf
val open_issues: MutableSet<String> = mutableSetOf("desc1", "desc2", "desc3")	// creates a val of a mut set

fun add_issue(uniq_desc: String): Boolean {	// receives new issue and returns true if it can be added
    return open_issues.add(uniq_desc)
}

fun get_status_log(is_added: Boolean): String {	// receives the result of the above fun
    return if (is_added) "registered correctly" else "marked as duplicate"
}

fun main(){
    val new_issue: String = "desc4" 
    val already_in_issue = "desc3"
    
    println(open_issues)
    println("issue $new_issue ${get_status_log(add_issue(new_issue))}")
    println("issue $already_in_issue ${get_status_log(add_issue(already_in_issue))}")
    println(open_issues)
}
