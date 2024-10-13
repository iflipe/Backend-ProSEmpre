// templates de string para replicar

const carroselEquipe = `
    <div class="profissional">
        <img src={imagem}> 
        <h3>{nome}</h3>
        <p>{profissao}</p>
        <p>{extraInfo}</p>
    </div>
`

const cardArtigo = `
    <div>
        <img class="card-artigo" src={imagem}>
        <p class="card-descricao">{descricao}</p>
    </div>
`

const cardTopicosPrincipais = `
                   <div class="carousel-cell">
    <div class="item-topico-popular">
        <div class="item-topico-popular-content">

            <div class="section-titulo-paragrafo-item-topico-popular">
                <h3>{titulo}</h3>
                <p>{conteudo}</p>
            </div>


            
            <div class="sections-item-topico-popular">
                <div class="item-topico-popular-section1">
                    <img src="../../img/icones/comentario-icon.png" alt="icone de comentário" class="comentario-icone-topico-popular" />
                    <p>{quantidadePessoas} discutindo esse tópico</p>
                </div>
                <div class="item-topico-popular-section2">
                    <img src="../../img/icones/relogio-icone.png" alt="icone de relogio" class="relogio-icone-topico-popular" />
                    <p>Criado há {quantidadeTempo}</p>
                </div>
            </div>


        </div>

    </div>
                </div>
`

const cardItemTopico = `
    <div class="item-topico">
        <div class="conteudo-item-topico">
            <h3>{titulo}</h3>
            <div class="perfil-item-topico">
                <div class="icone-perfil-item-topico {corFundoPerfil}">
                    <img src="{iconePerfil}" alt="icone do perfil">

                </div>
                <div class="texto-perfil-item-topico">
                    <p class="nome-perfil-item-topico">{username}</p>
                    <p class="tempo-postado-perfil-item-topico">{quandoPostou}</p>
                </div>
            </div>

            <div class="paragrafo-item-topico">
                <p>{conteudo}</p>
                <span>Ver mais <img class="icone-seta-pra-baixo-item-topicos" src="../../img/icones/seta-pra-baixo-icon.png" alt="icone de seta pra baixo"/></span>
            </div>

            <div class="footer-item-topico">
                <div class="icons-item-topico">
                    <img src="../../img/icones/salvar-icon.png" alt="icone de salvar" class="salvar-icon-item-topico">
                    <div class="add-comentario-item-topico">
                        <img src="../../img/icones/comentario-icon.png" alt="icone de comentario">
                        <p>Adicionar comentário</p>
                    </div>
                </div>

                
                <div class="footer-sugestao">
                    <p>Faça como {comentadoresEmComum} e {quantidadePessoas} e comente sobre <span>{titulo}</span></p>
                </div>

            </div>

        </div>

    </div>

`

const cards = `
    <div class="item">
        <img src={imagem}>
        <p class="my-paragraph">{descricao}</p>
    </div>
`
export { cardArtigo, carroselEquipe, cards, cardTopicosPrincipais, cardItemTopico }
