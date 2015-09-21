function port_top --description 'prints the process using the provided port'
	set -l pid (lsof -t -i:$argv[1])
	if count $pid >  /dev/null
		set -l cmd (ps -p $pid -o command | tail -n 1)
		ps -p $pid -o command 
		printf "PID: %s\n" $pid
		printf "CMD: %s\n" $cmd
	else
		set_color red; echo "Nothing on $argv[1]"; set_color normal
	end
end
