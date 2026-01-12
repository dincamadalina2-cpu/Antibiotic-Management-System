# Antibiotic Management System - Iteration 1

# class Antibiotic:
#     def __init__(self, name, drug_class, spectrum):
#         self.name = name
#         self.drug_class = drug_class
#         self.spectrum = spectrum
#
#
# # List of antibiotics (entities)
# antibiotics = [
#     Antibiotic("Amoxicillin", "Penicillin", "Broad"),
#     Antibiotic("Ciprofloxacin", "Fluoroquinolone", "Broad"),
#     Antibiotic("Vancomycin", "Glycopeptide", "Narrow"),
#     Antibiotic("Azithromycin", "Macrolide", "Broad"),
#     Antibiotic("Penicillin G", "Penicillin", "Narrow")
# ]
#
#
# def display_menu():
#     print("\n--- Antibiotic Management System ---")
#     print("1. Search antibiotic by name")
#     print("2. Filter antibiotics by spectrum")
#     print("3. Sort antibiotics alphabetically")
#     print("4. Exit")
#
#
# def search_antibiotic(name, antibiotics_list):
#     found = False
#     for a in antibiotics_list:
#         if a.name.lower() == name.lower():
#             print("Antibiotic found:")
#             print(a.name, "-", a.drug_class, "-", a.spectrum)
#             found = True
#             break
#     if not found:
#         print("Antibiotic not found")
#
#
# def filter_by_spectrum(spectrum, antibiotics_list):
#     print("\nAntibiotics with", spectrum, "spectrum:")
#     for a in antibiotics_list:
#         if a.spectrum.lower() == spectrum.lower():
#             print(a.name)
#
#
# def sort_antibiotics(antibiotics_list):
#     sorted_list = sorted(antibiotics_list, key=lambda x: x.name)
#     print("\nAntibiotics sorted alphabetically:")
#     for a in sorted_list:
#         print(a.name, "-", a.drug_class, "-", a.spectrum)
#
#
# running = True
# while running:
#     display_menu()
#     option = input("Choose option: ")
#
#     if option == "1":
#         name = input("Enter antibiotic name: ")
#         search_antibiotic(name, antibiotics)
#
#     elif option == "2":
#         spectrum = input("Enter spectrum (Broad/Narrow): ")
#         filter_by_spectrum(spectrum, antibiotics)
#
#     elif option == "3":
#         sort_antibiotics(antibiotics)
#
#     elif option == "4":
#         running = False
#         print("Exiting program...")
#
#     else:
#         print("Invalid option. Try again.")

# ---------------------------------------------------------- #
# Antibiotic Management System - Iteration 2 (CRUD)

# class Antibiotic:
#     def __init__(self, name, drug_class, spectrum):
#         self.name = name
#         self.drug_class = drug_class
#         self.spectrum = spectrum
#
#
# # Initial list (from Iteration 1)
# antibiotics = [
#     Antibiotic("Amoxicillin", "Penicillin", "Broad"),
#     Antibiotic("Ciprofloxacin", "Fluoroquinolone", "Broad"),
#     Antibiotic("Vancomycin", "Glycopeptide", "Narrow"),
# ]
#
#
# def display_menu():
#     print("\n--- Antibiotic Management System ---")
#     print("1. Add new antibiotic")
#     print("2. View all antibiotics")
#     print("3. Search antibiotic by name")
#     print("4. Update antibiotic")
#     print("5. Delete antibiotic")
#     print("6. Sort antibiotics alphabetically")
#     print("7. Exit")
#
#
# # CREATE
# def add_antibiotic(antibiotics_list):
#     name = input("Enter antibiotic name: ")
#     drug_class = input("Enter drug class: ")
#     spectrum = input("Enter spectrum (Broad/Narrow): ")
#
#     antibiotics_list.append(Antibiotic(name, drug_class, spectrum))
#     print("Antibiotic added successfully!")
#
#
# # READ
# def view_antibiotics(antibiotics_list):
#     if len(antibiotics_list) == 0:
#         print("No antibiotics available.")
#         return
#
#     for a in antibiotics_list:
#         print(a.name, "-", a.drug_class, "-", a.spectrum)
#
#
# def search_antibiotic(name, antibiotics_list):
#     for a in antibiotics_list:
#         if a.name.lower() == name.lower():
#             print("Found:", a.name, "-", a.drug_class, "-", a.spectrum)
#             return
#     print("Antibiotic not found")
#
#
# # UPDATE
# def update_antibiotic(name, antibiotics_list):
#     for a in antibiotics_list:
#         if a.name.lower() == name.lower():
#             print("Enter new details:")
#             a.drug_class = input("New drug class: ")
#             a.spectrum = input("New spectrum (Broad/Narrow): ")
#             print("Antibiotic updated successfully!")
#             return
#     print("Antibiotic not found")
#
#
# # DELETE
# def delete_antibiotic(name, antibiotics_list):
#     for a in antibiotics_list:
#         if a.name.lower() == name.lower():
#             antibiotics_list.remove(a)
#             print("Antibiotic deleted successfully!")
#             return
#     print("Antibiotic not found")
#
#
# # SORT
# def sort_antibiotics(antibiotics_list):
#     sorted_list = sorted(antibiotics_list, key=lambda x: x.name)
#     for a in sorted_list:
#         print(a.name, "-", a.drug_class, "-", a.spectrum)
#
#
# # Main program loop
# running = True
# while running:
#     display_menu()
#     option = input("Choose option: ")
#
#     if option == "1":
#         add_antibiotic(antibiotics)
#
#     elif option == "2":
#         view_antibiotics(antibiotics)
#
#     elif option == "3":
#         name = input("Enter antibiotic name: ")
#         search_antibiotic(name, antibiotics)
#
#     elif option == "4":
#         name = input("Enter antibiotic name to update: ")
#         update_antibiotic(name, antibiotics)
#
#     elif option == "5":
#         name = input("Enter antibiotic name to delete: ")
#         delete_antibiotic(name, antibiotics)
#
#     elif option == "6":
#         sort_antibiotics(antibiotics)
#
#     elif option == "7":
#         running = False
#         print("Exiting program...")
#
#     else:
#         print("Invalid option. Try again.")

# ---------------------------------------------------------- #

# Antibiotic Management System - Iteration 3 (Streamlit GUI)

import streamlit as st
import pandas as pd


# ---------------- ENTITY ----------------
class Antibiotic:
    def __init__(self, name, drug_class, spectrum):
        self.name = name
        self.drug_class = drug_class
        self.spectrum = spectrum


# ---------------- DATA STORAGE ----------------
if "antibiotics" not in st.session_state:
    st.session_state.antibiotics = [
    Antibiotic("Amoxicillin", "Penicillin", "Broad"),
    Antibiotic("Ampicillin", "Penicillin", "Broad"),
    Antibiotic("Penicillin G", "Penicillin", "Narrow"),
    Antibiotic("Penicillin V", "Penicillin", "Narrow"),
    Antibiotic("Ceftriaxone", "Cephalosporin", "Broad"),
    Antibiotic("Cefotaxime", "Cephalosporin", "Broad"),
    Antibiotic("Cefazolin", "Cephalosporin", "Narrow"),
    Antibiotic("Azithromycin", "Macrolide", "Broad"),
    Antibiotic("Clarithromycin", "Macrolide", "Broad"),
    Antibiotic("Erythromycin", "Macrolide", "Narrow"),
    Antibiotic("Vancomycin", "Glycopeptide", "Narrow"),
    Antibiotic("Teicoplanin", "Glycopeptide", "Narrow"),
    Antibiotic("Doxycycline", "Tetracycline", "Broad"),
    Antibiotic("Tetracycline", "Tetracycline", "Broad"),
    Antibiotic("Ciprofloxacin", "Fluoroquinolone", "Broad"),
    Antibiotic("Levofloxacin", "Fluoroquinolone", "Broad"),
    ]


# ---------------- TITLE ----------------
st.title("Antibiotic Management System")


# ---------------- MENU ----------------
menu = st.sidebar.selectbox(
    "Select operation",
    ["Search / Filter / Sort", "Read Antibiotics", "Create Antibiotic", "Update Antibiotic", "Delete Antibiotic", "View Charts"]
)
# ---------------- SEARCH / FILTER / SORT ----------------
if menu == "Search / Filter / Sort":
    st.subheader("Search, Filter, and Sort Antibiotics")

    # --- Search ---
    search_name = st.text_input("Search by Name")
    if search_name:
        results = [a for a in st.session_state.antibiotics if search_name.lower() in a.name.lower()]
        if results:
            st.write("Search Results")
            for a in results:
                st.write(f"{a.name} | {a.drug_class} | {a.spectrum}")
        else:
            st.warning("No antibiotics found with that name.")

    st.markdown("---")

    # --- Filter by Spectrum ---
    filter_spectrum = st.selectbox("Filter by Spectrum", ["All", "Broad", "Narrow"])
    filtered = st.session_state.antibiotics
    if filter_spectrum != "All":
        filtered = [a for a in filtered if a.spectrum == filter_spectrum]

    st.write(f"Filtered Antibiotics ({filter_spectrum})")
    for a in filtered:
        st.write(f"{a.name} | {a.drug_class} | {a.spectrum}")

    st.markdown("---")

    # --- Sort Alphabetically ---
    sort_option = st.radio("Sort Alphabetically?", ["No", "Yes"])
    display_list = filtered
    if sort_option == "Yes":
        display_list = sorted(filtered, key=lambda x: x.name)

    st.write("Sorted List")
    for a in display_list:
        st.write(f"{a.name} | {a.drug_class} | {a.spectrum}")


# ---------------- READ ----------------
if menu == "Read Antibiotics":
    st.subheader("All Antibiotics")
    st.subheader("Name | Class | Spectrum")

    if len(st.session_state.antibiotics) == 0:
        st.warning("No antibiotics available")
    else:
        for a in st.session_state.antibiotics:
            st.write(f"{a.name} | {a.drug_class} | {a.spectrum}")


# ---------------- CREATE ----------------
elif menu == "Create Antibiotic":
    st.subheader("Create New Antibiotic")

    name = st.text_input("Antibiotic Name")
    drug_class = st.text_input("Drug Class")
    spectrum = st.selectbox("Spectrum", ["Broad", "Narrow"])

    if st.button("Add"):
        if name != "":
            st.session_state.antibiotics.append(
                Antibiotic(name, drug_class, spectrum)
            )
            st.success("Antibiotic added successfully!")
        else:
            st.error("Name cannot be empty")


# ---------------- UPDATE ----------------
elif menu == "Update Antibiotic":
    st.subheader("Update Antibiotic")

    names = [a.name for a in st.session_state.antibiotics]

    if len(names) == 0:
        st.warning("No antibiotics to update")
    else:
        selected = st.selectbox("Select antibiotic", names)

        for a in st.session_state.antibiotics:
            if a.name == selected:
                new_class = st.text_input("New Drug Class", a.drug_class)
                new_spectrum = st.selectbox(
                    "New Spectrum", ["Broad", "Narrow"],
                    index=0 if a.spectrum == "Broad" else 1
                )

                if st.button("Update"):
                    a.drug_class = new_class
                    a.spectrum = new_spectrum
                    st.success("Antibiotic updated successfully!")


# ---------------- DELETE ----------------
elif menu == "Delete Antibiotic":
    st.subheader("Delete Antibiotic")

    names = [a.name for a in st.session_state.antibiotics]

    if len(names) == 0:
        st.warning("No antibiotics to delete")
    else:
        selected = st.selectbox("Select antibiotic to delete", names)

        if st.button("Delete"):
            st.session_state.antibiotics = [
                a for a in st.session_state.antibiotics if a.name != selected
            ]
            st.success("Antibiotic deleted successfully!")

# ---------------------------------------------------------- #
elif menu == "View Charts":
    st.title("Antibiotic Analysis Charts")

    # Chart 1
    st.subheader("Number of Antibiotics per Drug Class")
    classes = [a.drug_class for a in st.session_state.antibiotics]
    st.bar_chart(pd.Series(classes).value_counts())

    # Chart 2
    st.subheader("Broad vs Narrow Spectrum Antibiotics")
    spectrums = [a.spectrum for a in st.session_state.antibiotics]
    st.bar_chart(pd.Series(spectrums).value_counts())

    # Chart 3
    st.subheader("Spectrum Distribution per Drug Class")
    df = pd.DataFrame({
        "Class": classes,
        "Spectrum": spectrums
    })
    st.bar_chart(df.groupby(["Class", "Spectrum"]).size().unstack(fill_value=0))


