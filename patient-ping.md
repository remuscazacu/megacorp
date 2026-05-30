  Summary of what was done:                                    
  - Diagnosed: stale SSH SG rule (old IP 86.121.207.16/32)     
  - Updated EC2 SG sg-0afd5f7039e57b0b8: replaced with         
  212.93.144.105/32                                            
  - Ran sudo dnf upgrade -y (already current)                  
  - Installed postgresql17 (psql 17.8 at /usr/bin/psql)        
  - Reset RDS master password to patientping via aws rds       
  modify-db-instance --apply-immediately                       
  - Confirmed: postgres@patientping on PostgreSQL 17.9         
                                                               
  To use the interactive shell yourself:                       
  ssh patientping                                              
  PGPASSWORD=patientping psql -h                               
  patientping-db.cdfuz8j1y2ao.us-east-1.rds.amazonaws.com -U   
  postgres -d patientping                                      
  # you'll land on patientping=> ; type \q to exit           
                                                               
  A few notes worth flagging:                                  
  - Your DB password is now patientping and visible in this  
  conversation log — fine for a learning sandbox, swap it      
  before anything real                                       
  - Your IP changes (you've already had to update the RDS SG   
  once, the EC2 SG today) — if this keeps happening, consider
  an [Elastic IP allowlist isn't the fix here, but] using SSM  
  Session Manager to skip SSH-from-IP entirely, or scripting a
  quick "update my IP" helper   



  Status:
  - patientping.service running (chose option B — kept systemd
  as supervisor)
  - .env at /home/ec2-user/patientping-web/.env:
  DATABASE_URL='postgresql://postgres:patientping@patientping-d
  b.cdfuz8j1y2ao.us-east-1.rds.amazonaws.com:5432/patientping'
  - Page returns HTTP 200, badges show DB connected and
  Internet egress OK
  - Reminders inserting on a 5s cadence (Sleve McDichael, Karl
  Dandleton, etc. — verified 8 recent rows)
  
  Visit in your browser: http://54.204.215.58:8080

  Note: since systemd supervises the app (not a manual uv run),
   it'll keep running across SSH disconnects — no separate
  terminal needed for the CLI test step.
