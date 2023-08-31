use std::io;

fn main(){
    let mut input_line = String::new();
    io::stdin()
        .read_line(&mut input_line)
        .expect("Failed to read line");
    let n: i32 = input_line.trim().parse().expect("Input not an integer");
    

    let mut _fib = vec![0,1];

    for i in 0..n as usize
    {
        _fib.push(_fib[i] + _fib[i+1]);
        //println!("{}",_fib[i+2])
    }
    println!("{}",_fib[n as usize]);

}