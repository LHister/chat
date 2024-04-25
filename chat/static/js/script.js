let csrfToken = "{{ csrf_token }}";

function redirectToLoginPage() {
    // Redirect the user to the login page
    window.location.href = '/login'; // Replace '/login' with the actual URL of your login page
}

function showNamePrompt() {
    // Check if the prompt has already been shown
    if (!localStorage.getItem('namePromptShown')) {
        // Set the flag indicating that the prompt has been shown
        localStorage.setItem('namePromptShown', true);
        // Redirect the user to the login page
        redirectToLoginPage();
    }
}

showNamePrompt();

function cls(){
    document.getElementById("cls").addEventListener("click", function() {
        document.getElementById("messageInput").value = "monsterorderclear";
        document.getElementById("cls").submit();})
};

cls()

const greetings = ['{ Hello }', '{ ⴰⵎⴰⵣⵉⵖ }', '{ مرحبا }', '{ Hola }', '{ Ciao }', '{ Привет }', '{ 你好 }', '{ سلام }', '{ こんにちは }', '{ 안녕하세요 }', '{ नमस्ते }', '{ Bonjour }'];
let index = 0;
function lang_switch(){
    const ele_gret = document.querySelector('.gret');
    const cur_gret = greetings[index];
    const colors = ['red', 'chartreuse', '#0a49f6'];

    ele_gret.textContent = cur_gret
    ele_gret.style.color = colors[index % colors.length];

    index = (index + 1) % greetings.length;
    
}

lang_switch()
setInterval(lang_switch, 700);

function upl(){
    $(document).ready(function() {
        $('#file-input').on('change', function() {
            // Trigger form submission when a file is selected
            $('#uploadForm').submit();
        });
    });
}

upl()