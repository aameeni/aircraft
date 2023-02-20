import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the app function
def app():
    # Define user inputs
    st.header("777-200ER Charter Profit and Loss Statement")
    st.subheader("Enter your assumptions below:")
    
    # Define crew and expenses inputs
    crew = ['CAPTAIN', 'F/O', 'L/M', 'TECHNICIAN']
    crew_dict = {}
    for c in crew:
        crew_dict[c] = st.number_input(f"{c} salary per flight ($)", value=5000, step=1000)
    flight_time = st.number_input("Flight Time (H)", value=10, step=1)
    fuel_cost = st.number_input("Fuel cost per Kg ($)", value=0.35, step=0.01)
    landing_charge = st.number_input("Landing charge ($)", value=500, step=100)
    ramp_handling_charge = st.number_input("Ramp Handling charge ($)", value=500, step=100)
    cargo_handling_charge = st.number_input("Cargo Handling charge ($)", value=500, step=100)
    catering_charge = st.number_input("Catering charge ($)", value=500, step=100)
    parking_charge = st.number_input("Parking charge ($)", value=500, step=100)
    security_charge = st.number_input("Security charge ($)", value=500, step=100)
    noise_charge = st.number_input("Noise charge ($)", value=500, step=100)
    follow_me_charge = st.number_input("Follow Me charge ($)", value=500, step=100)
    push_back_charge = st.number_input("Push back charge ($)", value=500, step=100)
    navigation_terminal_charge = st.number_input("Navigation Terminal charge ($)", value=500, step=100)
    cargo_charge = st.number_input("Cargo Charge ($)", value=500, step=100)
    line_maintenance_charge = st.number_input("Line Maintenance charge ($)", value=500, step=100)
    lighting_charge = st.number_input("Lighting charge ($)", value=500, step=100)
    fuel_charge = st.number_input("Fuel charge ($)", value=0.35, step=0.01)
    hotel_cost = st.number_input("Hotel accommodations for crew ($)", value=1000, step=100)
    crew_transportation_cost = st.number_input("Crew Transportation ($)", value=500, step=100)
    uniform_cost = st.number_input("Uniform cost ($)", value=1000, step=100)
    office_expenses = st.number_input("Office expenses ($)", value=5000, step=1000)
    crew_salaries = sum(crew_dict.values())
    maintenance_reserve = st.number_input("Maintenance Reserve ($)", value=10000, step=1000)
    line_maintenance = st.number_input("Line Maintenance ($)", value=10000, step=1000)
    insurance = st.number_input("Insurance ($)", value=5000, step=1000)
    trip_costs = fuel_cost * 10000 + landing_charge + ramp_handling_charge + cargo_handling_charge + catering_charge + parking_charge + security_charge + noise_charge + follow_me_charge + push_back_charge + navigation_terminal_charge + cargo_charge + line_maintenance_charge + lighting_charge
    dry_lease = st.number_input("Dry Lease ($)", value=50000, step=1000)
    overheads = st.number_input("Overheads ($)", value=0, step=1)
    # Define revenue assumptions inputs
    st.subheader("Revenue assumptions:")
    passengers_per_flight = st.number_input("Passengers per flight", value=250, step=10)
    ticket_price = st.number_input("Ticket price per passenger ($)", value=1000, step=100)
    cargo_revenue = st.number_input("Cargo revenue per flight ($)", value=10000, step=1000)

    # Define function to calculate profit and loss statement
    @st.cache_data
    def calculate_profit_loss_statement(num_flights, num_aircrafts):
        revenue = (num_flights * passengers_per_flight * ticket_price) + (num_flights * cargo_revenue)
        expenses = (num_flights * flight_time * (crew_salaries / 4)) + (num_flights * fuel_cost * 10000) + (num_flights * landing_charge) + (num_flights * ramp_handling_charge) + (num_flights * cargo_handling_charge) + (num_flights * catering_charge) + (num_flights * parking_charge) + (num_flights * security_charge) + (num_flights * noise_charge) + (num_flights * follow_me_charge) + (num_flights * push_back_charge) + (num_flights * navigation_terminal_charge) + (num_flights * cargo_charge) + (num_flights * line_maintenance_charge) + (num_flights * lighting_charge) + (num_flights * dry_lease / num_aircrafts) + (num_flights * overheads) + (num_flights * (hotel_cost + crew_transportation_cost + uniform_cost) / 4) + (num_aircrafts * maintenance_reserve) + (num_flights * line_maintenance) + (num_flights * insurance)
        profit_loss = revenue - expenses
        return profit_loss

    # Define function to plot profit and loss statement
    @st.cache_data
    def plot_profit_loss_statement(pl_list):
        fig, ax = plt.subplots()
        ax.plot(pl_list)
        ax.set_title("Profit and Loss Statement")
        ax.set_xlabel("Year")
        ax.set_ylabel("Profit/Loss")
        return fig

    # Define user inputs for investment plan
    st.subheader("Investment Plan:")
    num_flights = st.number_input("Number of flights per year", value=500, step=50)
    num_aircrafts = st.number_input("Number of aircrafts", value=1, step=1)
    num_years = st.number_input("Number of years", value=5, step=1)

    # Calculate profit and loss statement
    pl_list = []
    for year in range(num_years):
        pl = calculate_profit_loss_statement(num_flights, num_aircrafts)
        pl_list.append(pl)

    # Display profit and loss statement table
    year_list = list(range(1, num_years+1))
    pl_df = pd.DataFrame({'Year': year_list, 'Profit/Loss': pl_list})
    st.dataframe(pl_df)

    # Plot profit and loss statement
    fig = plot_profit_loss_statement(pl_list)
    st.pyplot(fig)
    
    # Run the app
if __name__ == '__main__':
    app()