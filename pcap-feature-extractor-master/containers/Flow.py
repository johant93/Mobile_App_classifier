#inherits from Packet_container
from containers.PacketContainer import PacketContainer
from containers import Packet

class Flow(PacketContainer):

    # Class field - Packet container here
    packet_list = []
    start_time = 0
    times = []
    time_deltas = []
    size_array = []
    df = None

    def __init__(self, p):
        self.df = p

    def get_df(self):
        return self.df

    """ FIX """
    def generate_times(self):
        pass

    """  """
    def generate_time_deltas(self):
        pass

    """
    Return unbiased standard deviation of the packet flow time deltas.
    Normalized by N-1 by default. This can be changed using the ddof argument - pandas
    """
    def std_time_delta(self):
        return self.df['frame.time_delta'].std()

    """ Length in seconds """
    def duration(self):
        pass

    """ Total number of packets with payload """
    def pl_total_packets(self):
        pass

    """ Total number of packets without payload """
    def no_pl_total_packets(self):
        pass

    """ Size of all packets in bytes """
    def size(self):
        return self.df['frame.len'].sum()

    """ Amount of packets """
    def __len__(self):
        return len(self.df)

    """ Variance of packet size """
    def sizevar(self):
        return self.df['frame.len'].var()

    """ Min packet size """
    def min_packet_size(self):
        return self.df['frame.len'].min()

    """ Max packet size """
    def max_packet_size(self):
        return self.df['frame.len'].max()

    """ Std packet size """
    def std_packet_size(self):
        return self.df['frame.len'].std()

    """ Mean packet size """
    def mean_packet_size(self):
        return self.df['frame.len'].mean()

    """ Min time delta """
    def min_time_delta(self):
        return self.df['frame.time_delta'].min()

    """ Max time delta """
    def max_time_delta(self):
        return self.df['frame.time_delta'].max()

    """ time delta mean """
    def mean_time_delta(self):
        return self.df['frame.time_delta'].mean()
