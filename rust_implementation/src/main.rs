use std::fs::OpenOptions;
use std::fs;
use std::fs::File;
use std::io;
use std::path::Path;
use std::io::BufReader;
use std::io::BufRead;
use std::io::Write;


//Global Constants
const TEMP_FILE_NAME: &'static str = "../../TempDict.txt";
const DICTIONARY_NAME: &'static str = "../../Words.txt";


fn main() {
    clear_file();
    let num_letters = init_game();
    let dict = make_dictionary(num_letters);

}


//Make dictionary with only the correct number of letters
fn make_dictionary(num_letters : u8) -> File {
    File::create(TEMP_FILE_NAME).unwrap();
    let mut temp_dir = OpenOptions::new()
        .write(true)
        .append(true)
        .open(TEMP_FILE_NAME)
        .unwrap();
    let original_dir = File::open(DICTIONARY_NAME).unwrap();
    let buf = BufReader::new(&original_dir);
    for line in buf.lines() {
        let l = line.unwrap();
        if l.len() as u8 == num_letters {
            if let Err(_) = writeln!(temp_dir, "{}", l) {
                println!("{}", l);
            }
        }
    }

    return temp_dir;
}

//Get the original number of letters
fn init_game() -> u8 {
    let mut num_letters = String::new();
    println!("How many letters? : ");
    io::stdin().read_line(&mut num_letters).expect("Failed to read line");
    let num_letters: u8 = match num_letters.trim().parse() {
        Ok(num) => num,
        Err(_) => panic!("Please enter a number"),
    };
    if num_letters < 4 {
        panic!("Please enter a number >= 4.");
    }
    println!("num_letters : {}", num_letters);
    return num_letters;
}

//Remove the temp file if it exists
fn clear_file() {
    if Path::new(TEMP_FILE_NAME).exists() {
        fs::remove_file(TEMP_FILE_NAME).unwrap();
    }
}
