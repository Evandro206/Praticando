package Pratica01;

public class Livro {
    // Atributos
    private String titulo;
    private String autor;
    private String genero;
    private String editora;
    private int quantidade;

    // Construtor
    public Livro(String titulo, String autor, String genero, String editora, int quantidade) {
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
        this.editora = editora;
        this.quantidade = quantidade;
    }

    // Setters
    public void setTitulo(String titulo){
        this.titulo = titulo;
    }

    public void setAutor(String autor){
        this.autor = autor;
    }

    public void setGenero(String genero){
        this.genero = genero;
    }

    public void setEditora(String editora){
        this.editora = editora;
    }

    public void setQuantidade(int quantidade){
        this.quantidade = quantidade;
    }

    // Getters
    public String getTitulo(){
        return titulo;
    }

    public String getAutor(){
        return autor;
    }

    public String getGenero(){
        return genero;
    }

    public String getEditora(){
        return editora;
    }

    public int getQuantidade(){
        return quantidade;
    }

    // Método para exibir informações
    public void exibirInformações(){
        System.out.println("Titulo: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Genero: " + genero);
        System.out.println("Editora: " + editora);
        System.out.println("Disponibilidade: " + quantidade);
    }
}