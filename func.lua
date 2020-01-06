function coth (i) 
  return math.cosh(i) / math.sinh(i)
end

function brillouin (J, x) 
  if x == 0 then
    return 0
  else
   return (2*J+1)/(2*J)*coth((2*J+1)/(2*J)*x) - 
        1/(2*J)*coth(1/(2*J)*x)
  end
end

function T (r, a, x)
    return (a*a -2*a*r*cos(x) +r*r)/(1 - 2*a*r*cos(x) +a*a*r*r) 
end