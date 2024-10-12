
function renderizarDivs(id, data, template) { // substitui o conteúdo da div com o id escolhido pela lista
    // de elementos
    const elementoDaPagina = document.querySelector(`#${id}`)
    const listaDeElementos = data.map((item) => { 
        return modelarString(template, item)
    }).join("")
    
    elementoDaPagina.innerHTML = listaDeElementos
}

function modelarString(template, data) { // substitui tudo que está dentro de chaves na string template
    return template.replace(/\{(.*?)}/g, (match, key) => {
        return data[key] || ""
    })
}

export {renderizarDivs}