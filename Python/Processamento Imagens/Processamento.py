from PIL import Image, ImageFilter

def resize_image(input_path: str, output_path: str, size: tuple) -> None:
    """
    Redimensiona a imagem para o tamanho especificado.

    :param input_path: Caminho para a imagem de entrada.
    :param output_path: Caminho para salvar a imagem redimensionada.
    :param size: Tupla com o novo tamanho (largura, altura).
    """
    # Abre a imagem
    with Image.open(input_path) as img:
        # Redimensiona a imagem
        img_resized = img.resize(size)
        # Salva a imagem redimensionada
        img_resized.save(output_path)
    print(f"Imagem redimensionada e salva em {output_path}")

def apply_filter(input_path: str, output_path: str, filter_type: str) -> None:
    """
    Aplica um filtro à imagem.

    :param input_path: Caminho para a imagem de entrada.
    :param output_path: Caminho para salvar a imagem com filtro aplicado.
    :param filter_type: Tipo de filtro a ser aplicado ('blur', 'contour', etc.).
    """
    # Abre a imagem
    with Image.open(input_path) as img:
        # Aplica o filtro baseado no tipo
        if filter_type == 'blur':
            img_filtered = img.filter(ImageFilter.BLUR)
        elif filter_type == 'contour':
            img_filtered = img.filter(ImageFilter.CONTOUR)
        else:
            print("Filtro não reconhecido. Usando filtro padrão (blur).")
            img_filtered = img.filter(ImageFilter.BLUR)

        # Salva a imagem filtrada
        img_filtered.save(output_path)
    print(f"Filtro aplicado e imagem salva em {output_path}")
