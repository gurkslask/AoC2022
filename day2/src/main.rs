use std::fs;
use std::collections::HashMap;
fn main() {
    println!("Hello, world!");

    let contents = fs::read_to_string("input.txt")
        .expect("Shoud work");

    let contents = contents.split("\n");
    let shape = HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3),
    ]);
    let outcomes = HashMap::from([
        ("A", HashMap::from([ ("X", 3), ("Y", 6), ("Z", 0)  ])),
        ("B", HashMap::from([ ("X", 0), ("Y", 3), ("Z", 6)  ])),
        ("C", HashMap::from([ ("X", 6), ("Y", 0), ("Z", 3)  ])),
    ]);
    let mut score = 0;
    for row in contents{
        row.trim();
        let rr = row.split(" ").collect::<Vec<&str>>();
        println!("{}", rr[1]);
        score += shape[rr[1].trim()];
        score += outcomes[rr[0].trim()][rr[1].trim()];
    }
    println!("{score}");
}
