package Pratica01;

public class Main {
    // 
    public static void main() {
        // Registra um livro teste
        Livro livro = new Livro("Dom Quixote", "Miguel de Cervantes", "Romance", "Editora Aventura", 3);

        // Exibe informações do livro
        livro.exibirInformações();

        // Muda quantidade do livro e exibe a nova quantidade
        livro.setQuantidade(5);
        System.out.println("Nova quantidade: " + livro.getQuantidade());
    }
}