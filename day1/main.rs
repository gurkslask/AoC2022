use std::fs;

fn main(){
    let contents = fs::read_to_string("input.txt")
        .expect("Shoud work");

    let contents = contents.split("\n");
    let mut a: Vec<i32> = Vec::new();
    let mut t = 0;
    for row in contents {
        if row.len() > 1 {
            let rr = row.replace("\r", "");
            let ii = rr.parse::<i32>().unwrap();
            t += ii;
        } else {
            a.push(t);
            t = 0;
        }
    }
    let ll = a.len();
    println!("{ll}");
    for ii in &a { println!("{ii}")};
    let m = a.iter().max().unwrap();
    println!("{m}")
}