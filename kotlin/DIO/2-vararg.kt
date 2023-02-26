package me.dio.vararg_functions.kt

fun main(){

	fun print_all(vararg messages: String){	// vararg storages multiple values
		for (m in messages) println(m)
	}
	
	fun print_all_with_prefix(vararg messages: String, prefix: String) {
		for (m in messages) println(prefix + m)
	}
	
	fun Log(vararg entries: String){
		print_all(*entries)	// * passes entries as a vararg instead of array
	}
	
	print_all("Oi", "Hello", "Hola")
	print_all_with_prefix("oi", "Hello", "Hola", prefix = "message: ")
	Log("Oi", "Hello", "Hola")
}
