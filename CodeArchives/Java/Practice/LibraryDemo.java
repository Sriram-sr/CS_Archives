public class LibraryDemo {
    int id;
    String name;
    String book;
    String author;
    int rate;

    LibraryDemo(int id, String name, String book, String author, int rate){
        this(name, book, author, rate);
        this.id = id;
    }

    LibraryDemo(String name, String book, String author, int rate){
        this(book, author, rate);
        this.name = name;
    }

    LibraryDemo(String book, String author, int rate){
        this(author, rate);
        this.book = book;
    }

    LibraryDemo(String author, int rate){
        this.author = author;
        this.rate = rate;
    }

    void display(){
        System.out.println("The student("+id+") "+name+" has took "+book+" book written by "+author+" which costs "+rate);
    }

    public static void main(String args[]){
        // LibraryDemo book1 = new LibraryDemo(1, "Sriram", "TCP", "Forhan", 2500);
        LibraryDemo book1 = new LibraryDemo("behardeen", 2000);
        book1.display();
    }
}
