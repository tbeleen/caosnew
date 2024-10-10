function confirmarDelete(id){
    Swal.fire({
        title: "Estás seguro?",
        text: "Esta acción no se puede revertir!",
        icon: "error",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminar!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Eliminado!",
                text: "Noticia eliminada correctamente.",
                icon: "success"
            }).then(function(){
                window.location.href ="delete/" + id + "/";
            })
        }
    });
}

function confirmarDeletePerio(id){
    Swal.fire({
        title: "Estás seguro?",
        text: "Esta acción no se puede revertir!",
        icon: "error",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminar!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Eliminado!",
                text: "Periodista eliminado correctamente.",

                icon: "success"
            }).then(function(){
                window.location.href ="delete/" + id + "/";
            })
        }
    });
}

function confirmarDeletesoli(id){
    Swal.fire({
        title: "Estás seguro?",
        text: "Esta acción no se puede revertir!",
        icon: "error",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminar!"
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                title: "Eliminado!",
                text: "Periodista eliminado correctamente.",

                icon: "success"
            }).then(function(){
                window.location.href ="/delete/" + id + "/";
            })
        }
    });
}