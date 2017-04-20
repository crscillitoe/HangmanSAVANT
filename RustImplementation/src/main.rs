use std::fs;
use std::io;
use std::path::Path;
fn main() {
    clear_file();

    let mut num_letters = String::new();
    print!("How many letters? : ");
    io::stdin().read_line(&mut num_letters).expect("Failed to read line");
    let num_letters: u32 = match num_letters.trim().parse() {
        Ok(num) => num,
        Err(_) => panic!("Please enter a number"),
    };
    if num_letters < 4 {
        panic!("Please enter a number >= 4.");
    }
    println!("num_letters : {}", num_letters);

}


//Remove the temp file if it exists
fn clear_file() {
    let temp_dir_path = "../../TempDict.txt";
    if Path::new(temp_dir_path).exists() {
        fs::remove_file(temp_dir_path).unwrap();
    }
}
