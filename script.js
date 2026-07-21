document.addEventListener("DOMContentLoaded", () => {
    
    // 1. Animação de rolagem (Fade In)
    const observerOptions = { root: null, rootMargin: '0px', threshold: 0.1 };
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('appear');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(el => observer.observe(el));

    // 2. Lógica da Barra de Busca Drill Down
    const searchInput = document.getElementById('moduleSearch');
    const accordions = document.querySelectorAll('details.accordion');

    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            // Pega o texto digitado e converte para minúsculo
            const searchTerm = e.target.value.toLowerCase();

            accordions.forEach(accordion => {
                let hasMatchInAccordion = false;
                const rows = accordion.querySelectorAll('.info-item-row');
                
                // Se o próprio título da sanfona (ex: Gas Processing) bater com a busca, mostra tudo
                const summaryText = accordion.querySelector('summary').textContent.toLowerCase();
                const titleMatch = summaryText.includes(searchTerm);

                rows.forEach(row => {
                    const rowText = row.textContent.toLowerCase();
                    
                    // Se achar a palavra na linha ou se o título da sanfona bater
                    if (rowText.includes(searchTerm) || titleMatch) {
                        row.style.display = 'flex';
                        hasMatchInAccordion = true;
                    } else {
                        row.style.display = 'none';
                    }
                });

                // Se achou alguma coisa dentro desta categoria, mostra a categoria e abre a sanfona
                if (hasMatchInAccordion) {
                    accordion.style.display = 'block';
                    if (searchTerm !== '') {
                        accordion.setAttribute('open', 'true');
                    } else {
                        // Se apagar o texto da busca, fecha a sanfona de volta
                        accordion.removeAttribute('open');
                    }
                } else {
                    accordion.style.display = 'none'; // Esconde a categoria inteira se não achar nada
                }
            });
        });
    }
});
