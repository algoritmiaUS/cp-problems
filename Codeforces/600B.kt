# Problem: Queries about less or equal elements
# Solution by Kenny Jesús Flores Huamán
# url: https://codeforces.com/problemset/problem/600/B

fun binary_search(numbers: List<Int>, target: Int): Int {
    var left = 0
    var right = numbers.size - 1

    while (left <= right) {
        val mid = (left + right) / 2
        if (numbers[mid] <= target) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return left
}

fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val a = readln().split(" ").map { it.toInt() }.sorted()
    val b = readln().split(" ").map { it.toInt() }

    val result = b.map { binary_search(a, it) }
    println(result.joinToString(" "))
}
