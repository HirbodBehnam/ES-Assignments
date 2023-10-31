module GenerateModule(input wire clk, input wire reset, input wire a,input wire b,input wire c, output reg n_state, output reg p_state);
	localparam [4:0] init=4'b1000, secondry=4'b0100, blackhole=4'b0010, third=4'b0001;

	always @(*) begin
		case (p_state)
			init: begin
				if (a) begin
					n_state = secondry;
				end

			end
			secondry: begin
				if (c) begin
					n_state = third;
				end
				if (b) begin
					n_state = blackhole;
				end

			end
			blackhole: begin

			end
			third: begin
				if (c) begin
					n_state = blackhole;
				end

			end
		endcase
	end

	always @(posedge clk) begin
		if (reset)
			p_state <= init;
		else
			p_state <= n_state;
	end
endmodule
