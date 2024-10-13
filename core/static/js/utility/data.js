const artigos = [
    {
        imagem: "../img/home/artigos-e-materiais-home/artigo-1.png",
        descricao: "Lorem ipsum dolor sit amet, consectetur",
    },
    {
        imagem: "../img/home/artigos-e-materiais-home/artigo-2.png",
        descricao: "Lorem ipsum dolor sit amet, consectetur",
    },
    {
        imagem: "../img/home/artigos-e-materiais-home/artigo-3.png",
        descricao: "Lorem ipsum dolor sit amet, consectetur",
    },
]

const materiais = [
    {
        imagem: "../img/home/artigos-e-materiais-home/material-1.png",
        descricao: "Lorem ipsum dolor sit amet, consectetur",
    },
    {
        imagem: "../img/home/artigos-e-materiais-home/material-2.png",
        descricao: "Lorem ipsum dolor sit amet, consectetur",
    },
    {
        imagem: "../img/home/artigos-e-materiais-home/material-3.png",
        descricao: "Lorem ipsum dolor sit amet, consectetur",
    },
]

const profissionais = [
    {
        imagem: "../img/home/profissionais/equipe-isaac.png",
        nome: "isaac Lima",
        profissao: "Psicólogo Infantil",
        extraInfo: "CRP 0000000",
    },
    {
        imagem: "../img/home/profissionais/equipe-anelise.png",
        nome: "Annelise Figueiredo",
        profissao: "Pedagoga especializada",
        extraInfo: "em Ensino Bilingue",
    },
    {
        imagem: "../img/home/profissionais/equipe-malu.png",
        nome: "Malu Queiroz",
        profissao: "Nutricionista Infantil",
        extraInfo: "CRN 00000/P",
    },
    {
        imagem: "../img/home/profissionais/equipe-leo.png",
        nome: "Leonardo Matos",
        profissao: "Pediatra",
        extraInfo: "CRM/RN 000000",
    },
]

const topicosPrincipais = [
    {
        titulo: "Lorem ipsum dolor sit amet",
        conteudo: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at mauris quis magna aliquet condimentumt.",
        quantidadePessoas: "25",
        quantidadeTempo: "3 meses",
    },
    {
        titulo: "Lorem ipsum dolor sit amet",
        conteudo: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at mauris quis magna aliquet condimentumt.",
        quantidadePessoas: "25",
        quantidadeTempo: "3 meses",
    },
    {
        titulo: "Lorem ipsum dolor sit amet",
        conteudo: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at mauris quis magna aliquet condimentumt.",
        quantidadePessoas: "25",
        quantidadeTempo: "3 meses",
    },

]

const itemTopico = [
    {
        titulo: "Lorem ipsum dolor sit amet",
        iconePerfil: "../../img/icones/cavalo-icon.png",
        username: "Cavalo Anônimo",
        quandoPostou: "12h atrás",
        conteudo: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque autem doloribus ratione quae, fuga iure libero? Sint, rem cum esse velit amet explicabo, consequuntur totam voluptatibus quisquam est iste ratione.",
        comentadoresEmComum: ["Capivara Anônima", "Falcão Anônimo"],
        quantidadePessoas: "1",
        corFundoPerfil: "roxo"
    },
    {
        titulo: "Eject, lorem ipsum",
        iconePerfil: "../../img/icones/cervo-icon.png",
        username: "Cervo Anônimo",
        quandoPostou: "2 dias atrás",
        conteudo: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque autem doloribus ratione quae, fuga iure libero? Sint, rem cum esse velit amet explicabo, consequuntur totam voluptatibus quisquam est iste ratione.",
        comentadoresEmComum: ["Capivara Anônima", "Falcão Anônimo"],
        quantidadePessoas: "20",
        corFundoPerfil: "amarelo"
    }
]

// automatizar o singular e plural nos itens de topicos e juntar o nome dos comentadores
itemTopico.forEach(e=>{
    e.comentadoresEmComum = e.comentadoresEmComum.join(", ")
    const pessoas = Number(e.quantidadePessoas)
    pessoas > 1 ? e.quantidadePessoas = `outras ${e.quantidadePessoas} pessoas` : e.quantidadePessoas = `outra ${e.quantidadePessoas} pessoa`

})


// para automatizar o singular e plural da frase em topicos principais
topicosPrincipais.forEach(element => {
    const pessoas = Number(element.quantidadePessoas)
    pessoas > 1 ? element.quantidadePessoas += " pessoas estão" : element.quantidadePessoas += " pessoa está"
});

const cardsColorir =[
    {
        imagem:"../img/pais-e-profs/image-01-colorir.png",
        descricao: "Alfabeto",
    },
    {
        imagem:"../img/pais-e-profs/image-02-colorir.png",
        descricao: "Natureza",
    },
    {
        imagem:"../img/pais-e-profs/image-03-colorir.png",
        descricao: "Brincadeiras"
    }
]

const cardsMaterias = [
    {
        imagem:"../img/pais-e-profs/image-01-materias.png",
        descricao: "Português",
    },
    {
        imagem:"../img/pais-e-profs/image-02-materias.png",
        descricao: "Matemática",
    },
    {
        imagem:"../img/pais-e-profs/image-03-materias.png",
        descricao: "História",
    }
]

export { artigos, materiais, profissionais, topicosPrincipais, itemTopico, cardsColorir, cardsMaterias }
