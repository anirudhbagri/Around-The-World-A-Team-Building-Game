
import random

def get_source_destination_pair(world_tour_route: list, num_of_countries):
    source_destination_pair, z = [], 0
    for i in range(num_of_countries):
        source_destination_pair.append([world_tour_route[i], world_tour_route[i+1]])
        z = z+1
        if z == num_of_countries:
            break
    return source_destination_pair

def partition_source_destination(source_destination_list, num_of_poles):
    random.shuffle(source_destination_list)
    return [source_destination_list[i::num_of_poles] for i in range(num_of_poles)]

def print_docs(source_destiantion_pair: list, counter_num):
    from fpdf import FPDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf_w=210
    pdf_h=297
    pdf.rect(5.0, 5.0, 200.0,287.0)
    pdf.set_xy(0.0,0.0)
    pdf.set_font('Arial', 'B', 24)
    pdf.set_text_color(220, 50, 50)
    pdf.cell(w=210.0, h=40.0, align='C', txt=f"AROUND THE WORLD - COUNTER {counter_num}", border=0)
    pdf.ln(36)
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(95, 24, str("Source"), border=1, align='C')
    pdf.cell(95, 24, str("Destination"), border=1, align='C')
    pdf.ln(24)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 20)
    for source_destination in source_destiantion_pair:
        for name in source_destination:
            pdf.cell(95, 24, str(name), border=1, align='C')    
        pdf.ln(24)
    pdf.output(f"Counter_{counter_num}.pdf", 'F')

def main():
    num_of_poles = int(input("Enter number of poles (default 4): ") or "4")
    num_of_countries = num_of_poles * 9
    with open("ListOfCountries.txt") as file:
        complete_list_of_countries = [line.rstrip() for line in file.readlines()]
    list_of_countries = random.sample(complete_list_of_countries, num_of_countries)
    print("==  World Tour Route ==\n")
    for i in list_of_countries:
        print(i, "->", end=" ")
    print("\n\n")
    list_of_countries.append(list_of_countries[0])
    source_destination_pair = get_source_destination_pair(list_of_countries, num_of_countries)
    for idx, i in enumerate(partition_source_destination(source_destination_pair, num_of_poles)):
        print(i)
        print_docs(i, idx+1)

if __name__ == "__main__":
    main()
