import { renderizarDivs } from "./utility/utils"

import { profissionais, artigos, materiais, topicosPrincipais, itemTopico, cardsColorir, cardsMaterias } from "./utility/data"
import { carroselEquipe, cardArtigo, cardTopicosPrincipais, cardItemTopico, cards } from "./utility/templates"

document.addEventListener("DOMContentLoaded", function() {
const root = document.querySelector("#app")

function renderizarCarrossel(){
    const script1 = document.createElement('script');
    script1.src = 'https://unpkg.com/flickity@2/dist/flickity.pkgd.min.js';
    script1.async = true;
    document.body.appendChild(script1);

    const script2 = document.createElement('script');
    script2.src = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js';
    script2.async = true;
    document.body.appendChild(script2);
}

// Função para renderizar a página com base no nome
function renderizar(pagina) {
    fetch(`./paginas/${pagina}/${pagina}.html`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Erro ao carregar a página")
            }
            return response.text()
        })
        .then(data => {
            root.innerHTML = data

            // aplica os scripts do carrossel em todas as paginas
            renderizarCarrossel();
            
            if (pagina === "home") {
                renderizarDivs("profissionais", profissionais, carroselEquipe) 
                renderizarDivs("artigos", artigos, cardArtigo)
                renderizarDivs("materiais", materiais, cardArtigo)
            } else if(pagina ==="pais-e-profs"){
                renderizarDivs("cards-didaticos", cardsColorir, cards )
                renderizarDivs("cards-materias", cardsMaterias, cards )
            }
            if(pagina === "forum"){
                renderizarDivs("topicos-populares", topicosPrincipais, cardTopicosPrincipais)
                renderizarDivs("topicos", itemTopico, cardItemTopico)
            }
            
        })
        .catch(error => {
            console.error(error)
            root.innerHTML = "<p>Erro ao carregar a página. Tente novamente mais tarde.</p>"
        });
}

    // Função para lidar com cliques nos botões da navbar
    function setupNavButtons() {
        document.querySelector("#home").addEventListener("click", () => {
            renderizar("home")
            history.pushState(null, "", "/home") // Atualiza a URL
        });

        document.querySelector("#videos").addEventListener("click", () => {
            renderizar("videos")
            history.pushState(null, "", "/videos") // Atualiza a URL
        });

        document.querySelector("#forum").addEventListener("click", () => {
            renderizar("forum")
            history.pushState(null, "", "/forum") // Atualiza a URL
        });

        document.querySelector("#pais-e-profs").addEventListener("click", () => {
            renderizar("pais-e-profs")
            history.pushState(null, "", "/pais-e-profs") // Atualiza a URL
        });
    }

    // Verifica o path atual e renderiza o conteúdo correspondente ao carregar a página
    const pathAtual = window.location.pathname

    if (pathAtual === "/videos") {
        renderizar("videos")
    } else if (pathAtual === "/forum") {
        renderizar("forum")
    } else if (pathAtual === "/pais-e-profs") {
        renderizar("pais-e-profs")
    } else {
        renderizar("home");  // Carrega "home" por padrão
    }

    // Configura os botões da navbar
    setupNavButtons()

    // Lida com navegação de "voltar" e "avançar" no histórico
    window.addEventListener("popstate", function() {
        const pathAtual = window.location.pathname

        if (pathAtual === "/videos") {
            renderizar("videos")
        } else if (pathAtual === "/forum") {
            renderizar("forum")
        } else if (pathAtual === "/pais-e-profs") {
            renderizar("pais-e-profs")
        } else {
            renderizar("home"); // Carrega "home" por padrão
        }
    })
})
