package me.dio.null_safety.kt

fun check_string(str: String?): String{
	if (str != null && str.length > 0){
		return "String: $str \nLength: ${str.length}" // \n breaks line
	} else {
		return "Empty or null string!"
	}
}

fun main(){
	var never_null: String = "This can't be null"	// when you explicity declare the variable can't be null
	// never_null = null generates an error
	
	var nullable: String? = "This can be null"	// ? says that the variable can be null
	nullable = null	// doesn't generate an error
	
	var inferred_non_null = "The compiler infers that this can't be null"
	// inferred_non_null = null generates an error
	
	fun str_len(str: String?): Int {
		return str?.length ?: 0	// ? accepts a null value for str and ?: returns 0 if str is null
	}
	
	println(str_len(never_null))
	println(str_len(nullable))
	println(check_string(inferred_non_null))
}
