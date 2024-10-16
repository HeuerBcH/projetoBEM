document.getElementById("menu-toggle").addEventListener("click", function() {
    const sidebar = document.getElementById("sidebar");
    const button = this; // Referência ao botão

    sidebar.classList.toggle("open");

    // Adiciona ou remove a classe 'active' ao botão
    if (sidebar.classList.contains("open")) {
        button.classList.add("active"); // Adiciona a classe 'active' se a sidebar estiver aberta
    } else {
        button.classList.remove("active"); // Remove a classe 'active' se a sidebar estiver fechada
        // Fecha dropdown se a sidebar for fechada
        document.querySelectorAll('.sidebar ul li').forEach(item => {
            item.classList.remove('active'); // Remove a classe active
            const dropdown = item.querySelector('.dropdown');
            if (dropdown) {
                dropdown.style.display = 'none'; // Esconde o dropdown
            }
        });
    }
});

document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
    toggle.addEventListener('click', function(e) {
        e.preventDefault(); // Evita o comportamento padrão do link
        
        const sidebar = document.getElementById("sidebar");
        if (!sidebar.classList.contains("open")) return; // Se a sidebar não estiver aberta, não faz nada

        const parentLi = this.parentElement;
        parentLi.classList.toggle('active'); // Alterna a classe active
        
        // Alterna a visibilidade da dropdown
        const dropdown = parentLi.querySelector('.dropdown');
        if (dropdown.style.display === 'block') {
            dropdown.style.display = 'none';
        } else {
            dropdown.style.display = 'block';
        }
    });
});

document.querySelector('.logout-button').addEventListener('click', function() {
    // Redireciona para a página de logout
    window.location.href = '/logout'; // Altere para a URL correta
});

document.querySelectorAll('.view-turmas').forEach(item => {
    item.addEventListener('click', function() {
        window.location.href = this.getAttribute('href');
    });
});