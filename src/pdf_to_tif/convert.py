import sys
import fitz
from PIL import Image


def get_signature_sizes(page_count, num_signatures):
    total = max(((page_count + 3) // 4) * 4, 4 * num_signatures)
    units = total // 4
    base = units // num_signatures
    remainder = units % num_signatures
    sizes = [(base + 1) * 4 if i < remainder else base * 4
             for i in range(num_signatures)]
    return sizes, total


def get_booklet_order(sig_size):
    sheets = []
    for i in range(sig_size // 2):
        if i % 2 == 0:
            left = sig_size - i
            right = i + 1
        else:
            left = i + 1
            right = sig_size - i
        sheets.append((left, right))
    return sheets


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert.py <input.pdf> [signatures]")
        sys.exit(1)

    num_signatures = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    doc = fitz.open(sys.argv[1])
    page_count = len(doc)
    sig_sizes, total = get_signature_sizes(page_count, num_signatures)

    sample = doc[0]
    zoom = 300 / 72
    pw, ph = int(sample.rect.width * zoom), int(sample.rect.height * zoom)
    mat = fitz.Matrix(zoom, zoom)

    sheet_index = 0
    page_offset = 0

    for sig_num, sig_size in enumerate(sig_sizes):
        sheets = get_booklet_order(sig_size)
        for left_local, right_local in sheets:
            left_global = left_local + page_offset
            right_global = right_local + page_offset
            spread = Image.new("RGB", (pw * 2, ph), (255, 255, 255))
            for j, page_num in enumerate([left_global, right_global]):
                if 1 <= page_num <= page_count:
                    pix = doc[page_num - 1].get_pixmap(matrix=mat, alpha=False)
                    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                    spread.paste(img, (j * pw, 0))
            sig_index = f"{sig_num + 1:0{len(str(num_signatures))}d}"
            spread.save(f"booklet-{sig_index}-{sheet_index:03d}-{left_global}-{right_global}.tif", compression="tiff_lzw")
            print(f"Created booklet-{sheet_index:03d}.tif (sig {sig_num + 1}: {left_global} | {right_global})")
            sheet_index += 1
        page_offset += sig_size

    doc.close()


if __name__ == "__main__":
    main()
