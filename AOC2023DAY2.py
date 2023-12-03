#import libraries
import pandas as pd
import matsplotlib.pyplot as plt

#use network_traffic.csv as data for dataframe
#network_traffic.csv is a network packet log, 100 rows by 5 columns(PacketNumber,Timestamp, Source, Destination, Protocol)

df = pd.read_csv("network_traffic.csv")

#How many packets were captured (by looking at PacketNumber?)
packetcount = df.count()
print(packetcount)

#What IP address sent the most amount of traffic during the packet capture?
df.groupby(['Source']).size()

#What was the most frequent protocol?
df['Protocol'].size()

#OR

df['Protocol'].value_counts()
