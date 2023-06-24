const form = document.getElementById('nueva_persona');
    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Evita el envío del formulario
        const formData = new FormData(form);
        const personaData = {};

        for (let [key, value] of formData.entries()) {
            personaData[key] = value;
        }

        try {
            const response = await fetch('/personas', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json' //Para indicar que va en json
                },
                body: JSON.stringify(personaData) //Convertir en json
            });

            if (response.ok) {
                // Persona agregada correctamente
                alert('Persona agregada correctamente');
            } else {
                // Error en la respuesta del servidor
                const responseData = await response.json();
                alert(responseData.detail);
            }
        } catch (error) {
            // Error de conexión o solicitud
            console.error(error);
            alert('Error en la solicitud');
        }
    });