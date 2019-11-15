const sendBtn = document.getElementById('send_btn');
const textInput = document.getElementById('message_field');
const msgBoard = document.getElementById('msg_board');

	
function createMessageHTML(content, position) {
	const messageHTML = `<div class="d-flex justify-content-` + position + ` mb-4">
						    <div class="msg_cotainer">`
						        + content +
						    `</div>
						</div>`

	let template = document.createElement('template');
	template.innerHTML = messageHTML;
	return template.content.firstChild;
}



async function askUselessBot(message) {
	msgBoard.appendChild(createMessageHTML(message, 'end'));
	fetch('/bot?msg=' + encodeURIComponent(message))
		.then(resp => resp.json()) // transform the data into json
		.then(data => {
			msgBoard.appendChild(createMessageHTML(data['response']))
		})
		.catch(error => {
			console.error(error)
		})
}

sendBtn.addEventListener('click', (event) => {
	console.log("Sending Request...")
	let userQuestion = textInput.value.trim();
	if (userQuestion == '') {
		console.error('Empty input. TODO: flash msg');
		return ;
	}
	console.log(askUselessBot(userQuestion))
	textInput.value = '';
})